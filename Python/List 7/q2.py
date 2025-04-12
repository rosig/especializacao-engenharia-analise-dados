NUMBER_RUNNERS = 4


def get_runners_info_dict():
    dict_runners = {}  # {name: [times]}

    for num in range(NUMBER_RUNNERS):
        dict_runners.update(
            {
                input(f"Nome do corredor {num}: "): [
                    float(input("Tempo 1: ")),
                    float(input("Tempo 2: ")),
                    float(input("Tempo 3: ")),
                ]
            }
        )

    return dict_runners


def calculate_average(time_list):
    return sum(time_list) / len(time_list)


def find_winner():
    winner = ("", float("inf"))
    dict_runners = get_runners_info_dict()

    for name, time_list in dict_runners.items():
        average = calculate_average(time_list)
        if average < winner[1]:
            winner = (name, average)

    print(
        f"O campeão é {winner[0].upper()} com média de tempo de {winner[1]:.2f} segundos."
    )


find_winner()
