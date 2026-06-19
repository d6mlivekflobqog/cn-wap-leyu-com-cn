"""
tools/site_summary.py
读取内置站点资料并输出结构化摘要
"""

SITES = [
    {
        "url": "https://cn-wap-leyu.com.cn",
        "keywords": ["乐鱼体育"],
        "tags": ["体育", "娱乐", "赛事"],
        "description": "综合性体育娱乐平台，提供赛事资讯与互动服务。",
        "language": "zh-CN",
        "category": "entertainment"
    },
    {
        "url": "https://example-sports.org",
        "keywords": ["体育赛事", "实时比分"],
        "tags": ["体育", "比分", "新闻"],
        "description": "实时体育比分与赛事新闻聚合站点。",
        "language": "en",
        "category": "sports"
    }
]


def format_site_summary(site: dict) -> str:
    """
    格式化单个站点的摘要文本。
    """
    url = site.get("url", "未知")
    keywords = site.get("keywords", [])
    tags = site.get("tags", [])
    desc = site.get("description", "无描述")
    lang = site.get("language", "未知")
    cat = site.get("category", "未分类")

    kw_str = "、".join(keywords) if keywords else "无关键词"
    tag_str = "、".join(tags) if tags else "无标签"

    lines = [
        f"站点地址：{url}",
        f"核心关键词：{kw_str}",
        f"标签：{tag_str}",
        f"说明：{desc}",
        f"语言：{lang}，类别：{cat}",
        ""
    ]
    return "\n".join(lines)


def generate_full_summary(sites: list) -> str:
    """
    生成所有站点的完整结构化摘要。
    """
    header = "========== 内置站点资料摘要 =========="
    separator = "----------------------------------------"
    parts = [header]

    for idx, site in enumerate(sites, 1):
        title = f"站点 {idx}"
        parts.append(title)
        parts.append(separator)
        parts.append(format_site_summary(site))
        parts.append(separator)

    footer = "========== 摘要结束 =========="
    parts.append(footer)
    return "\n".join(parts)


def print_summary() -> None:
    """
    将摘要输出到标准输出。
    """
    summary = generate_full_summary(SITES)
    print(summary)


if __name__ == "__main__":
    print_summary()