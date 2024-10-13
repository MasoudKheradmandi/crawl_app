
def crawl_rss(websites):
    globals = {}
    exec(websites.code,globals)
    my_list = globals["my_list"]
    return my_list

