import re
from functools import reduce

NON_BREAKING_SPACE = '\u00A0'

def prettify_single_quotes(text):
    return re.sub(r"'(.*?)'", r'«\1»', text)

def prettify_double_quotes(text):
    return re.sub(r'"(.*?)"', r'«\1»', text)

def remove_extra_line_breaks(text):
    lines = [line.strip() for line in text.splitlines()]
    return '\r\n'.join(list(filter(None, lines)))

def remove_extra_spaces(text):
    return re.sub(r' {2,}', r' ', text)

def replace_hyphens_with_dashes_in_phone_numbers(text):
    return re.sub(r'\s*((\+?\d)?[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}[\s.,!?]*',
                  lambda m: re.sub(r'-', r'–', m.group(0)), text)

def replace_hyphens_with_dashes(text):
    return re.sub(r'\s-\s', r' — ', text)

def bind_numbers_with_following_words_by_non_breaking_spaces(text):
    return re.sub(r'(\d+)\s([а-яА-ЯёЁa-zA-Z]+)',
                  r'\1{}\2'.format(NON_BREAKING_SPACE), text)

def bind_conjunctions_with_following_words_by_non_breaking_spaces(text):
    return re.sub(r'([а-яА-ЯёЁa-zA-Z]{2,})\s([а-яА-ЯёЁa-zA-Z])',
                  r'\1{}\2'.format(NON_BREAKING_SPACE), text)

def apply_handlers(text, handlers):
    return reduce(lambda x,y: y(x), handlers, text)

def prepare_text_for_publication(text):
    handlers = [prettify_single_quotes,
                prettify_double_quotes,
                remove_extra_line_breaks,
                remove_extra_spaces,
                replace_hyphens_with_dashes_in_phone_numbers,
                replace_hyphens_with_dashes,
                bind_numbers_with_following_words_by_non_breaking_spaces,
                bind_conjunctions_with_following_words_by_non_breaking_spaces]
    return apply_handlers(text, handlers)
