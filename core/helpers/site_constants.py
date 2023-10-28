from html_sanitizer.sanitizer import sanitize_href, bold_span_to_strong, italic_span_to_em, tag_replacer, target_blank_noopener

html_sanitizer_settings = {
    "tags": {
        "header", "footer", "nav", "main", "section", "article", "aside",
        "ul", "ol", "li", "a", "h1", "h2", "h3", "h4", "h5", "h6", "p", "blockquote", "cite", "q", "em", "strong",
        "s", "u", "small",
        "img", "audio",
        "sub", "sup", "var", "code", "pre", "textarea",
        "div", "span", "br", "hr",
        "details", "summary",
        "table", "tbody", "tr", "th", "td"
    },
    "attributes": {
        "header": ("id", "class", "title"),
        "footer": ("id", "class", "title"),
        "nav": ("id", "class", "title"),
        "main": ("id", "class", "title"),
        "section": ("id", "class", "title"),
        "article": ("id", "class", "title"),
        "aside": ("id", "class", "title"),
        "ul": ("id", "class", "title"),
        "ol": ("id", "class", "title"),
        "li": ("id", "class", "title"),
        "a": ("href", "target", "title", "id", "class", "rel"),
        "h1": ("id", "class", "title"),
        "h2": ("id", "class", "title"),
        "h3": ("id", "class", "title"),
        "h4": ("id", "class", "title"),
        "h5": ("id", "class", "title"),
        "h6": ("id", "class", "title"),
        "p": ("id", "class", "title"),
        "blockquote": ("id", "class", "title"),
        "cite": ("id", "class", "title"),
        "q": ("id", "class", "title"),
        "em": ("id", "class", "title"),
        "strong": ("id", "class", "title"),
        "s": ("id", "class", "title"),
        "u": ("id", "class", "title"),
        "small": ("id", "class", "title"),
        "img": ("src", "id", "class", "title", "alt", "height", "width"),
        "audio": ("id", "class", "title", "controls", "src", "preload"),
        "sub": ("id", "class", "title"),
        "sup": ("id", "class", "title"),
        "var": ("id", "class", "title"),
        "code": ("id", "class", "title"),
        "pre": ("id", "class", "title"),
        "textarea": ("id", "class", "title", "name", "cols", "rows"),
        "div": ("id", "class", "title", "style"),
        "span": ("id", "class", "title", "style"),
        "br": ("id", "class", "title"),
        "hr": ("id", "class", "title"),
        "details": ("id", "class", "title"),
        "summary": ("id", "class", "title"),
        "table": ("id", "class", "title"),
        "tbody": ("id", "class", "title"),
        "tr": ("id", "class", "title"),
        "th": ("id", "class", "title"),
        "td": ("id", "class", "title")
    },
    "empty": {"hr", "a", "br", "img", "audio"},
    "separate": {"a", "p", "li"},
    "whitespace": {"br"},
    "keep_typographic_whitespace": True,
    "add_nofollow": False,
    "autolink": False,
    "sanitize_href": sanitize_href,
    "element_preprocessors": [
        # convert span elements into em/strong if a matching style rule
        # has been found. strong has precedence, strong & em at the same
        # time is not supported
        bold_span_to_strong,
        italic_span_to_em,
        tag_replacer("b", "strong"),
        tag_replacer("i", "em"),
        tag_replacer("form", "p"),
        target_blank_noopener,
    ],
    "element_postprocessors": [],
    "is_mergeable": lambda e1, e2: False,
}

strict_html_sanitizer_settings = {
    "tags": {
        "strong", "em", "p", "br", "b"
    },
    "attributes": {
    },
    "empty": {"br"},
    "separate": {"p"},
    "whitespace": {"br"},
    "keep_typographic_whitespace": True,
    "add_nofollow": False,
    "autolink": False,
    "sanitize_href": sanitize_href,
    "element_preprocessors": [
        # convert span elements into em/strong if a matching style rule
        # has been found. strong has precedence, strong & em at the same
        # time is not supported
        bold_span_to_strong,
        italic_span_to_em,
        tag_replacer("b", "strong"),
        tag_replacer("i", "em"),
        target_blank_noopener,
    ],
    "element_postprocessors": [],
    "is_mergeable": lambda e1, e2: False,
}
