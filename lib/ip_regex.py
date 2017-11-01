import re

from .dot_dict import DotDict


def _clean_regexp(item):
    result = None
    if isinstance(item, dict):
        result = DotDict()
        for key, value in item.items():
            result[key] = _clean_regexp(value)
    elif isinstance(item, CompiledReType):
        pattern = item.pattern
        pattern = pattern.replace(' ', '').replace('\r', '').replace('\n', '')
        result = sublime_re_pattern_sub.sub(':', pattern)
    else:
        raise TypeError('{}'.format(type(item)))
    return result


ip = DotDict({
    'v4': {
        'host': re.compile(r"""
                    (?xi)
                    (?:
                        (?!
                            (?:128\.0\.0\.0)|
                            (?:192\.0\.0\.0)|
                            (?:224\.0\.0\.0)|
                            (?:240\.0\.0\.0)|
                            (?:248\.0\.0\.0)|
                            (?:252\.0\.0\.0)|
                            (?:254\.0\.0\.0)|
                            (?:255\.0\.0\.0)|
                            (?:255\.128\.0\.0)|
                            (?:255\.192\.0\.0)|
                            (?:255\.224\.0\.0)|
                            (?:255\.240\.0\.0)|
                            (?:255\.248\.0\.0)|
                            (?:255\.252\.0\.0)|
                            (?:255\.254\.0\.0)|
                            (?:255\.255\.0\.0)|
                            (?:255\.255\.128\.0)|
                            (?:255\.255\.192\.0)|
                            (?:255\.255\.224\.0)|
                            (?:255\.255\.240\.0)|
                            (?:255\.255\.248\.0)|
                            (?:255\.255\.252\.0)|
                            (?:255\.255\.254\.0)|
                            (?:255\.255\.255\.0)|
                            (?:255\.255\.255\.128)|
                            (?:255\.255\.255\.192)|
                            (?:255\.255\.255\.224)|
                            (?:255\.255\.255\.240)|
                            (?:255\.255\.255\.248)|
                            (?:255\.255\.255\.252)|
                            (?:255\.255\.255\.254)|
                            (?:255\.255\.255\.255)|
                            (?:127\.255\.255\.255)|
                            (?:63\.255\.255\.255)|
                            (?:31\.255\.255\.255)|
                            (?:15\.255\.255\.255)|
                            (?:7\.255\.255\.255)|
                            (?:3\.255\.255\.255)|
                            (?:1\.255\.255\.255)|
                            (?:0\.255\.255\.255)|
                            (?:0\.127\.255\.255)|
                            (?:0\.63\.255\.255)|
                            (?:0\.31\.255\.255)|
                            (?:0\.15\.255\.255)|
                            (?:0\.7\.255\.255)|
                            (?:0\.3\.255\.255)|
                            (?:0\.1\.255\.255)|
                            (?:0\.0\.255\.255)|
                            (?:0\.0\.127\.255)|
                            (?:0\.0\.63\.255)|
                            (?:0\.0\.31\.255)|
                            (?:0\.0\.15\.255)|
                            (?:0\.0\.7\.255)|
                            (?:0\.0\.3\.255)|
                            (?:0\.0\.1\.255)|
                            (?:0\.0\.0\.255)|
                            (?:0\.0\.0\.127)|
                            (?:0\.0\.0\.63)|
                            (?:0\.0\.0\.31)|
                            (?:0\.0\.0\.15)|
                            (?:0\.0\.0\.7)|
                            (?:0\.0\.0\.3)|
                            (?:0\.0\.0\.1)|
                            (?:0\.0\.0\.0)
                        )
                        (?:(?:[1-2]?\d{1,2}\.){3}[1-2]?\d{1,2})
                    )
        """),
        'any': re.compile(
            r"""
            (?xi)
            (?:
                (?:
                    (?:
                        (?:
                            (?:host)|
                            (?:range)
                        )
                        \s+
                    )?
                    (?P<ip>
                        (?:
                            (?!
                                (?:128\.0\.0\.0)|
                                (?:192\.0\.0\.0)|
                                (?:224\.0\.0\.0)|
                                (?:240\.0\.0\.0)|
                                (?:248\.0\.0\.0)|
                                (?:252\.0\.0\.0)|
                                (?:254\.0\.0\.0)|
                                (?:255\.0\.0\.0)|
                                (?:255\.128\.0\.0)|
                                (?:255\.192\.0\.0)|
                                (?:255\.224\.0\.0)|
                                (?:255\.240\.0\.0)|
                                (?:255\.248\.0\.0)|
                                (?:255\.252\.0\.0)|
                                (?:255\.254\.0\.0)|
                                (?:255\.255\.0\.0)|
                                (?:255\.255\.128\.0)|
                                (?:255\.255\.192\.0)|
                                (?:255\.255\.224\.0)|
                                (?:255\.255\.240\.0)|
                                (?:255\.255\.248\.0)|
                                (?:255\.255\.252\.0)|
                                (?:255\.255\.254\.0)|
                                (?:255\.255\.255\.0)|
                                (?:255\.255\.255\.128)|
                                (?:255\.255\.255\.192)|
                                (?:255\.255\.255\.224)|
                                (?:255\.255\.255\.240)|
                                (?:255\.255\.255\.248)|
                                (?:255\.255\.255\.252)|
                                (?:255\.255\.255\.254)|
                                (?:255\.255\.255\.255)|
                                (?:127\.255\.255\.255)|
                                (?:63\.255\.255\.255)|
                                (?:31\.255\.255\.255)|
                                (?:15\.255\.255\.255)|
                                (?:7\.255\.255\.255)|
                                (?:3\.255\.255\.255)|
                                (?:1\.255\.255\.255)|
                                (?:0\.255\.255\.255)|
                                (?:0\.127\.255\.255)|
                                (?:0\.63\.255\.255)|
                                (?:0\.31\.255\.255)|
                                (?:0\.15\.255\.255)|
                                (?:0\.7\.255\.255)|
                                (?:0\.3\.255\.255)|
                                (?:0\.1\.255\.255)|
                                (?:0\.0\.255\.255)|
                                (?:0\.0\.127\.255)|
                                (?:0\.0\.63\.255)|
                                (?:0\.0\.31\.255)|
                                (?:0\.0\.15\.255)|
                                (?:0\.0\.7\.255)|
                                (?:0\.0\.3\.255)|
                                (?:0\.0\.1\.255)|
                                (?:0\.0\.0\.255)|
                                (?:0\.0\.0\.127)|
                                (?:0\.0\.0\.63)|
                                (?:0\.0\.0\.31)|
                                (?:0\.0\.0\.15)|
                                (?:0\.0\.0\.7)|
                                (?:0\.0\.0\.3)|
                                (?:0\.0\.0\.1)|
                                (?:0\.0\.0\.0)
                            )
                            (?:(?:\d{1,3}\.){3}\d{1,3})
                        )|
                        (?:(?:(?:(?:[0-9a-f]{1,4}:){7}(?:[0-9a-f]{1,4}|:))|(?:(?:[0-9a-f]{1,4}:){6}(?::[0-9a-f]{1,4}|(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3})|:))|(?:(?:[0-9a-f]{1,4}:){5}(?:(?:(?::[0-9a-f]{1,4}){1,2})|:(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3})|:))|(?:(?:[0-9a-f]{1,4}:){4}(?:(?:(?::[0-9a-f]{1,4}){1,3})|(?:(?::[0-9a-f]{1,4})?:(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3}))|:))|(?:(?:[0-9a-f]{1,4}:){3}(?:(?:(?::[0-9a-f]{1,4}){1,4})|(?:(?::[0-9a-f]{1,4}){0,2}:(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3}))|:))|(?:(?:[0-9a-f]{1,4}:){2}(?:(?:(?::[0-9a-f]{1,4}){1,5})|(?:(?::[0-9a-f]{1,4}){0,3}:(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3}))|:))|(?:(?:[0-9a-f]{1,4}:){1}(?:(?:(?::[0-9a-f]{1,4}){1,6})|(?:(?::[0-9a-f]{1,4}){0,4}:(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3}))|:))|(?::(?:(?:(?::[0-9a-f]{1,4}){1,7})|(?:(?::[0-9a-f]{1,4}){0,5}:(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3}))|:)))(?:%.+)?)
                    )
                )
                (?:
                    (?:
                        /
                        (?P<prefix_length>
                            \d{1,3}
                        )
                    )|
                    (?:
                        \s+
                        (?:
                            (?:mask\s+)?
                            (?:
                                (?P<netmask>
                                    (?:
                                        (?:0\.0\.0\.0)|
                                        (?:128\.0\.0\.0)|
                                        (?:192\.0\.0\.0)|
                                        (?:224\.0\.0\.0)|
                                        (?:240\.0\.0\.0)|
                                        (?:248\.0\.0\.0)|
                                        (?:252\.0\.0\.0)|
                                        (?:254\.0\.0\.0)|
                                        (?:255\.0\.0\.0)|
                                        (?:255\.128\.0\.0)|
                                        (?:255\.192\.0\.0)|
                                        (?:255\.224\.0\.0)|
                                        (?:255\.240\.0\.0)|
                                        (?:255\.248\.0\.0)|
                                        (?:255\.252\.0\.0)|
                                        (?:255\.254\.0\.0)|
                                        (?:255\.255\.0\.0)|
                                        (?:255\.255\.128\.0)|
                                        (?:255\.255\.192\.0)|
                                        (?:255\.255\.224\.0)|
                                        (?:255\.255\.240\.0)|
                                        (?:255\.255\.248\.0)|
                                        (?:255\.255\.252\.0)|
                                        (?:255\.255\.254\.0)|
                                        (?:255\.255\.255\.0)|
                                        (?:255\.255\.255\.128)|
                                        (?:255\.255\.255\.192)|
                                        (?:255\.255\.255\.224)|
                                        (?:255\.255\.255\.240)|
                                        (?:255\.255\.255\.248)|
                                        (?:255\.255\.255\.252)|
                                        (?:255\.255\.255\.254)|
                                        (?:255\.255\.255\.255)
                                    )
                                )|
                                (?P<wildcard>
                                    (?:
                                      (?:127\.255\.255\.255)|
                                      (?:63\.255\.255\.255)|
                                      (?:31\.255\.255\.255)|
                                      (?:15\.255\.255\.255)|
                                      (?:7\.255\.255\.255)|
                                      (?:3\.255\.255\.255)|
                                      (?:1\.255\.255\.255)|
                                      (?:0\.255\.255\.255)|
                                      (?:0\.127\.255\.255)|
                                      (?:0\.63\.255\.255)|
                                      (?:0\.31\.255\.255)|
                                      (?:0\.15\.255\.255)|
                                      (?:0\.7\.255\.255)|
                                      (?:0\.3\.255\.255)|
                                      (?:0\.1\.255\.255)|
                                      (?:0\.0\.255\.255)|
                                      (?:0\.0\.127\.255)|
                                      (?:0\.0\.63\.255)|
                                      (?:0\.0\.31\.255)|
                                      (?:0\.0\.15\.255)|
                                      (?:0\.0\.7\.255)|
                                      (?:0\.0\.3\.255)|
                                      (?:0\.0\.1\.255)|
                                      (?:0\.0\.0\.255)|
                                      (?:0\.0\.0\.127)|
                                      (?:0\.0\.0\.63)|
                                      (?:0\.0\.0\.31)|
                                      (?:0\.0\.0\.15)|
                                      (?:0\.0\.0\.7)|
                                      (?:0\.0\.0\.3)|
                                      (?:0\.0\.0\.1)|
                                      (?:0\.0\.0\.0)
                                    )
                                )
                            )
                        )
                    )
                )?
            )
            """
        ),
        'network': re.compile(
            r"""
            (?xi)
            (?:
                (?P<ip>
                    (?:
                        (?!
                            (?:128\.0\.0\.0)|
                            (?:192\.0\.0\.0)|
                            (?:224\.0\.0\.0)|
                            (?:240\.0\.0\.0)|
                            (?:248\.0\.0\.0)|
                            (?:252\.0\.0\.0)|
                            (?:254\.0\.0\.0)|
                            (?:255\.0\.0\.0)|
                            (?:255\.128\.0\.0)|
                            (?:255\.192\.0\.0)|
                            (?:255\.224\.0\.0)|
                            (?:255\.240\.0\.0)|
                            (?:255\.248\.0\.0)|
                            (?:255\.252\.0\.0)|
                            (?:255\.254\.0\.0)|
                            (?:255\.255\.0\.0)|
                            (?:255\.255\.128\.0)|
                            (?:255\.255\.192\.0)|
                            (?:255\.255\.224\.0)|
                            (?:255\.255\.240\.0)|
                            (?:255\.255\.248\.0)|
                            (?:255\.255\.252\.0)|
                            (?:255\.255\.254\.0)|
                            (?:255\.255\.255\.0)|
                            (?:255\.255\.255\.128)|
                            (?:255\.255\.255\.192)|
                            (?:255\.255\.255\.224)|
                            (?:255\.255\.255\.240)|
                            (?:255\.255\.255\.248)|
                            (?:255\.255\.255\.252)|
                            (?:255\.255\.255\.254)|
                            (?:255\.255\.255\.255)|
                            (?:127\.255\.255\.255)|
                            (?:63\.255\.255\.255)|
                            (?:31\.255\.255\.255)|
                            (?:15\.255\.255\.255)|
                            (?:7\.255\.255\.255)|
                            (?:3\.255\.255\.255)|
                            (?:1\.255\.255\.255)|
                            (?:0\.255\.255\.255)|
                            (?:0\.127\.255\.255)|
                            (?:0\.63\.255\.255)|
                            (?:0\.31\.255\.255)|
                            (?:0\.15\.255\.255)|
                            (?:0\.7\.255\.255)|
                            (?:0\.3\.255\.255)|
                            (?:0\.1\.255\.255)|
                            (?:0\.0\.255\.255)|
                            (?:0\.0\.127\.255)|
                            (?:0\.0\.63\.255)|
                            (?:0\.0\.31\.255)|
                            (?:0\.0\.15\.255)|
                            (?:0\.0\.7\.255)|
                            (?:0\.0\.3\.255)|
                            (?:0\.0\.1\.255)|
                            (?:0\.0\.0\.255)|
                            (?:0\.0\.0\.127)|
                            (?:0\.0\.0\.63)|
                            (?:0\.0\.0\.31)|
                            (?:0\.0\.0\.15)|
                            (?:0\.0\.0\.7)|
                            (?:0\.0\.0\.3)|
                            (?:0\.0\.0\.1)|
                            (?:0\.0\.0\.0)
                        )
                        (?:(?:\d{1,3}\.){3}\d{1,3})
                    )|
                    (?:(?:(?:(?:[0-9a-f]{1,4}:){7}(?:[0-9a-f]{1,4}|:))|(?:(?:[0-9a-f]{1,4}:){6}(?::[0-9a-f]{1,4}|(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3})|:))|(?:(?:[0-9a-f]{1,4}:){5}(?:(?:(?::[0-9a-f]{1,4}){1,2})|:(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3})|:))|(?:(?:[0-9a-f]{1,4}:){4}(?:(?:(?::[0-9a-f]{1,4}){1,3})|(?:(?::[0-9a-f]{1,4})?:(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3}))|:))|(?:(?:[0-9a-f]{1,4}:){3}(?:(?:(?::[0-9a-f]{1,4}){1,4})|(?:(?::[0-9a-f]{1,4}){0,2}:(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3}))|:))|(?:(?:[0-9a-f]{1,4}:){2}(?:(?:(?::[0-9a-f]{1,4}){1,5})|(?:(?::[0-9a-f]{1,4}){0,3}:(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3}))|:))|(?:(?:[0-9a-f]{1,4}:){1}(?:(?:(?::[0-9a-f]{1,4}){1,6})|(?:(?::[0-9a-f]{1,4}){0,4}:(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3}))|:))|(?::(?:(?:(?::[0-9a-f]{1,4}){1,7})|(?:(?::[0-9a-f]{1,4}){0,5}:(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3}))|:)))(?:%.+)?)
                )
                (?:
                    (?:
                        /
                        (?P<prefix_length>
                            \d{1,3}
                        )
                    )|
                    (?:
                        \s+
                        (?:
                            (?:mask\s+)?
                            (?:
                                (?P<netmask>
                                    (?:
                                        (?:0\.0\.0\.0)|
                                        (?:128\.0\.0\.0)|
                                        (?:192\.0\.0\.0)|
                                        (?:224\.0\.0\.0)|
                                        (?:240\.0\.0\.0)|
                                        (?:248\.0\.0\.0)|
                                        (?:252\.0\.0\.0)|
                                        (?:254\.0\.0\.0)|
                                        (?:255\.0\.0\.0)|
                                        (?:255\.128\.0\.0)|
                                        (?:255\.192\.0\.0)|
                                        (?:255\.224\.0\.0)|
                                        (?:255\.240\.0\.0)|
                                        (?:255\.248\.0\.0)|
                                        (?:255\.252\.0\.0)|
                                        (?:255\.254\.0\.0)|
                                        (?:255\.255\.0\.0)|
                                        (?:255\.255\.128\.0)|
                                        (?:255\.255\.192\.0)|
                                        (?:255\.255\.224\.0)|
                                        (?:255\.255\.240\.0)|
                                        (?:255\.255\.248\.0)|
                                        (?:255\.255\.252\.0)|
                                        (?:255\.255\.254\.0)|
                                        (?:255\.255\.255\.0)|
                                        (?:255\.255\.255\.128)|
                                        (?:255\.255\.255\.192)|
                                        (?:255\.255\.255\.224)|
                                        (?:255\.255\.255\.240)|
                                        (?:255\.255\.255\.248)|
                                        (?:255\.255\.255\.252)|
                                        (?:255\.255\.255\.254)|
                                        (?:255\.255\.255\.255)
                                    )
                                )|
                                (?P<wildcard>
                                    (?:
                                      (?:127\.255\.255\.255)|
                                      (?:63\.255\.255\.255)|
                                      (?:31\.255\.255\.255)|
                                      (?:15\.255\.255\.255)|
                                      (?:7\.255\.255\.255)|
                                      (?:3\.255\.255\.255)|
                                      (?:1\.255\.255\.255)|
                                      (?:0\.255\.255\.255)|
                                      (?:0\.127\.255\.255)|
                                      (?:0\.63\.255\.255)|
                                      (?:0\.31\.255\.255)|
                                      (?:0\.15\.255\.255)|
                                      (?:0\.7\.255\.255)|
                                      (?:0\.3\.255\.255)|
                                      (?:0\.1\.255\.255)|
                                      (?:0\.0\.255\.255)|
                                      (?:0\.0\.127\.255)|
                                      (?:0\.0\.63\.255)|
                                      (?:0\.0\.31\.255)|
                                      (?:0\.0\.15\.255)|
                                      (?:0\.0\.7\.255)|
                                      (?:0\.0\.3\.255)|
                                      (?:0\.0\.1\.255)|
                                      (?:0\.0\.0\.255)|
                                      (?:0\.0\.0\.127)|
                                      (?:0\.0\.0\.63)|
                                      (?:0\.0\.0\.31)|
                                      (?:0\.0\.0\.15)|
                                      (?:0\.0\.0\.7)|
                                      (?:0\.0\.0\.3)|
                                      (?:0\.0\.0\.1)|
                                      (?:0\.0\.0\.0)
                                    )
                                )
                            )
                        )
                    )
                )
            )
            """
        ),
    }
})

sublime_ip = DotDict()

sublime_re_pattern_sub = re.compile(r'P<[^>]+>')
CompiledReType = type(sublime_re_pattern_sub)

sublime_ip = _clean_regexp(ip)
