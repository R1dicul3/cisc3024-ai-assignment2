"""AI Assignment #2 — 候选算法检索/核验脚本

用途：为报告第 (1) 节 "how AI finds the algorithm" 留下**可复现**的检索证据链。
特征：走 arXiv 官方 API + GitHub 官方 API 做原始核验（不依赖搜索摘要，避免幻觉）。
用法：python tools/find_candidates.py
"""
import urllib.request, urllib.parse, json, time, re, os, sys
import xml.etree.ElementTree as ET

NS = {"a": "http://www.w3.org/2005/Atom"}
UA = {"User-Agent": "Mozilla/5.0 (dsh-research)"}
# arXiv 官方要求请求间隔 >= 3 秒
PACE = 3.5


def get(url, timeout=40, tries=5):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            last = e
            time.sleep(4 + i * 4)
    raise last


def arxiv_search(query, n=8, sort="submittedDate"):
    url = ("http://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(query)
           + f"&start=0&max_results={n}&sortBy={sort}&sortOrder=descending")
    root = ET.fromstring(get(url))
    out = []
    for e in root.findall("a:entry", NS):
        out.append({
            "title": " ".join(e.find("a:title", NS).text.split()),
            "published": e.find("a:published", NS).text[:10],
            "updated": e.find("a:updated", NS).text[:10],
            "id": e.find("a:id", NS).text.rsplit("/", 1)[-1],
            "summary": " ".join(e.find("a:summary", NS).text.split()),
        })
    return out


def arxiv_by_id(ids):
    url = "http://export.arxiv.org/api/query?id_list=" + ",".join(ids) + "&max_results=30"
    root = ET.fromstring(get(url))
    out = []
    for e in root.findall("a:entry", NS):
        s = " ".join(e.find("a:summary", NS).text.split())
        out.append({
            "title": " ".join(e.find("a:title", NS).text.split()),
            "published": e.find("a:published", NS).text[:10],
            "id": e.find("a:id", NS).text.rsplit("/", 1)[-1],
            "code": re.findall(r"(?:https?://)?github\.com/[\w\-./]+", s, re.I),
            "summary": s,
        })
    return out


def github_repo(full):
    try:
        d = json.loads(get(f"https://api.github.com/repos/{full}", timeout=25, tries=2))
        return {"full_name": d["full_name"], "stars": d["stargazers_count"],
                "pushed": d["pushed_at"][:10], "lang": d["language"],
                "desc": (d.get("description") or "")[:120]}
    except Exception as e:
        return {"full_name": full, "error": f"{type(e).__name__}"}


DISCOVERY = [
    ('Bayesian + classification + cs.CV', 'cat:cs.CV AND abs:"Bayesian" AND abs:"classification"'),
    ('variational + posterior + cs.CV',   'abs:"variational" AND abs:"posterior" AND cat:cs.CV'),
    ('probabilistic + classifier + cs.CV', 'cat:cs.CV AND abs:"probabilistic" AND abs:"classifier"'),
]

FINALISTS = ["2503.10080", "2404.11599", "2603.07911", "2602.01279",
             "2510.23684", "2605.06333", "2305.15241"]

REPOS = ["xiaozhen228/Bayes-PFL", "VectorInstitute/vbll", "less-and-less-bugs/CGBC",
         "fadel/viking", "huanranchen/DiffusionClassifier", "shouvik-sardar/TinyBayes"]


def main():
    log = []
    def say(s=""):
        print(s)
        log.append(s)

    say("=" * 70)
    say("PART 1 — arXiv DISCOVERY (newest first)")
    say("=" * 70)
    for label, q in DISCOVERY:
        say(f"\n--- {label} ---")
        try:
            for p in arxiv_search(q, n=8):
                say(f"  [{p['published']}] {p['title'][:96]}  ({p['id']})")
        except Exception as e:
            say(f"  ERROR {e}")
        time.sleep(PACE)

    say("\n" + "=" * 70)
    say("PART 2 — FINALIST DETAIL (abstract + code links)")
    say("=" * 70)
    for p in arxiv_by_id(FINALISTS):
        say(f"\n### {p['id']} | pub={p['published']}")
        say(f"  TITLE: {p['title']}")
        say(f"  CODE : {p['code'] if p['code'] else 'none in abstract'}")
        say(f"  ABS  : {p['summary'][:400]}")

    say("\n" + "=" * 70)
    say("PART 3 — GITHUB REPO HEALTH")
    say("=" * 70)
    for r in REPOS:
        d = github_repo(r)
        if "error" in d:
            say(f"  FAIL {d['full_name']} ({d['error']})")
        else:
            say(f"  OK   {d['full_name']} | stars={d['stars']} | pushed={d['pushed']} | lang={d['lang']}")
            say(f"       {d['desc']}")
        time.sleep(0.6)

    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(os.path.dirname(here), "logs")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "arxiv_github_search.log")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(log))
    print(f"\n[saved] {out}")


if __name__ == "__main__":
    main()
