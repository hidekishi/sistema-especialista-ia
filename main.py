import sys
from pyke import knowledge_engine, krb_traceback

engine = knowledge_engine.engine(__file__)


def bc_test():
    engine.reset()
    engine.activate("rules")

    try:
        with engine.prove_goal("rules.what_to_play($game)") as gen:
            for vars_, _ in gen:
                print(f"Voce deveria jogar: {vars_['game']}")
    except Exception as e:
        krb_traceback.print_exc()
        raise e


def main():
    print("EXPERT SYSTEM")
    bc_test()
    print("DONE")


if __name__ == "__main__":
    main()
