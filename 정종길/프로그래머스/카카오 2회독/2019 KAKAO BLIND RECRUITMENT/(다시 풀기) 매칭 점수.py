import re

def solution(word, pages):
    urls = {}
    links = []
    basic_point = []
    links_point = []
    
    word = word.lower()
    
    for idx, page in enumerate(pages):
        cnt = 0
        page = page.lower()
        
        match = re.search(r'<meta[^>]+content="([^"]+)"', page)
        if match:
            my_url = match.group(1)
            urls[my_url] = idx
        
        find_links = re.findall(r'<a[^>]+href="([^"]+)"', page)
        links.append(find_links)
        
        for w in re.findall(r'[a-z]+', page):
            if w == word:
                cnt += 1
                
        basic_point.append(cnt)
        # 링크 점수 계산 (ZeroDivisionError 방지)
        links_point.append(cnt / len(find_links) if find_links else 0)
    
    res = basic_point[:]
    
    for idx, link_list in enumerate(links):
        for link in link_list:
            linked_idx = urls.get(link, None)
            if linked_idx is not None:
                res[linked_idx] += links_point[idx]
    
    return res.index(max(res))
