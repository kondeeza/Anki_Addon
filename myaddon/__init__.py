from aqt import gui_hooks
from anki.cards import Card


def myfunc(card: Card) -> None:
  print("myfunc")


gui_hooks.reviewer_did_show_answer.append(myfunc)