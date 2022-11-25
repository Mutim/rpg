import textwrap


def word_wrap(args):
    n: list = textwrap.wrap(
        args,
        51,
        break_long_words=True)
    f = []
    for chunk in n:
        f.append(f' ║  {"".join([a for a in chunk]): <55}  ║')
    return "\n".join([a for a in f])


def event_text(message):
    text = f"""
■╠═══════════════════════════════════════════════════════════╣■
 ║  {'Strange Chest of Thieves': <40}                 ║
 ║                                                           ║
{word_wrap(message)}
 ║                                                           ║
■╠═══════════════════════════════════════════════════════════╣■
    """
    return text


print(event_text("This is a long message"))
