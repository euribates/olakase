#!/usr/bin/env python3

from datetime import date as Date
from datetime import datetime as DateTime

from django import template
from django.utils.safestring import mark_safe

import markdown


register = template.Library()


@register.filter
def as_boolean(value: bool) -> str:
    """representación textual de un campo lógico.
    """
    if value:
        return mark_safe('<strong class="bool-on">☑ Si</strong>')
    else:
        return mark_safe('<strong class="bool-off">☐ No</strong>')


@register.filter
def as_markdown(text: str) -> str:
    """Texto interpretado como Mardown.
    """
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


@register.filter
def as_date(dt: Date|DateTime) -> str:
    """Representación textual de una fecha.
    """
    return f'{dt.day}/{dt.month}/{dt.year}'
