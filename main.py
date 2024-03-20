from random import choice
from pyke import knowledge_engine, krb_traceback

engine = knowledge_engine.engine(__file__)


def bc_test():
    engine.reset()
    engine.activate("rules")

    try:
        with engine.prove_goal("rules.what_to_play($game)") as gen:
            vars_, _ = next(gen, (None, None))
            if vars_ is not None:
                game = vars_["game"]
                print(f"Você deveria jogar: {vars_['game']}")
            else:
                joga_nada = [
                    "Ah, não joga nada então",
                    "Então vai ler um livro",
                    "Vai dar uma volta na quadra",
                ]
                print(choice(joga_nada))
    except Exception as e:
        krb_traceback.print_exc()
        raise e


def main():
    print("EXPERT SYSTEM")
    bc_test()


if __name__ == "__main__":
    main()
