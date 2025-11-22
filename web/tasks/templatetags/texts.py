#!/usr/bin/env python3

from django import template
from django.utils.safestring import mark_safe

import markdown


register = template.Library()


@register.filter
def as_boolean(value):
    if value:
        return mark_safe('<strong class="bool-on">☑ Si</strong>')
    else:
        return mark_safe('<strong class="bool-off">☐ No</strong>')


@register.filter
def as_markdown(text):
    text = text.strip()
    text = text.replace(':\n', ':\n\n')
    text = text.replace('.\n', '.\n\n')
    if not hasattr(as_markdown, 'md_processor'):
        as_markdown.md_processor = markdown.Markdown(
            extras=['tables', 'footnotes']
        )
    result = as_markdown.md_processor.convert(text)
    if '<table' in result:
        result = result.replace('<table', '<table class="table"')
    return mark_safe(result)
