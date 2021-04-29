class CustomItemResolver:
    @staticmethod
    def resolve_item(linked_item):
        if linked_item.content_type == "article":
            return f"<h1>{linked_item.elements.title.value}</h1>"

        if linked_item.content_type == "tweet":
            return ("<blockquote class=\"twitter-tweet\" data-lang=\"en\""
                    f"data-theme={linked_item.elements.theme.value[0].codename}>"
                    f"<a href={linked_item.elements.tweet_link.value}></a></blockquote>")

        if linked_item.content_type == "hosted_video":
            return ("<div><iframe type=\"text/html\" width=\"640\" height=\"385\"" 
                     "style=\"display:block; margin: auto; margin-top:30px ; margin-bottom: 30px\"" 
                     f"src=\"https://www.youtube.com/embed/{linked_item.elements.video_id.value}?autoplay=1\"" 
                     "frameborder=\"0\"></iframe></div>")
