from random import choice
from pyke import knowledge_engine, krb_traceback

# inicializacao da knowlege engine
engine = knowledge_engine.engine(__file__)


# executar backwards-chaining
def bc():
    # para permitir que possa executar mais que uma vez
    engine.reset()
    # obtendo regras do arquivo "rules.krb"
    engine.activate("rules")

    try:
        with engine.prove_goal("rules.what_to_play($game)") as gen:
            # tentamos obter somente a primeira sugestão
            vars_, _ = next(gen, (None, None))
            if vars_ is not None:
                game = vars_["game"]
                print(f"Você deveria jogar: {game}")
            # se não existe, então não for possível sugerir um jogo
            # exibe uma mensagem para informar
            else:
                joga_nada = [
                    "Não joga nada então",
                    "Então vai ler um livro",
                    "Vai dar uma volta na quadra",
                ]
                print(choice(joga_nada))
    except Exception as e:
        # exibir traceback do pyke em caso de erro
        krb_traceback.print_exc()
        raise e


def main():
    print("Sistema Especialista para Recomendação de Jogos")
    bc()


if __name__ == "__main__":
    main()
