from typing import List

from output.output_colors import OutputColors
from ranking import Ranking, Problem, UndoableRanking


def add_contestant_wrapper(ranking: Ranking):
    def wrapped(p1, p2, p3, **kwargs):
        p1 = int(p1)
        p2 = int(p2)
        p3 = int(p3)
        try:
            ranking.add_contestant(p1, p2, p3)
        except ValueError as e:
            print(OutputColors.FAIL + e + OutputColors.ENDC)

    return wrapped


def list_contestants_wrapper(ranking: Ranking):
    def wrapped(**kwargs):
        for index in range(len(ranking.contestants)):
            print('{}.'.format(index), ranking.contestants[index].p1, ranking.contestants[index].p2, ranking.contestants[index].p3)

    return wrapped


def list_filter_contestants_wrapper(ranking: Ranking):
    def wrapped(sign, score, **kwargs):
        score = int(score)
        if sign == '<':
            for contestant in ranking.contestants:
                if contestant.average < score:
                    print(contestant.p1, contestant.p2, contestant.p3)
        elif sign == '=':
            for contestant in ranking.contestants:
                if contestant.average == score:
                    print(contestant.p1, contestant.p2, contestant.p3)
        elif sign == '>':
            for contestant in ranking.contestants:
                if contestant.average > score:
                    print(contestant.p1, contestant.p2, contestant.p3)

    return wrapped


def list_sorted_contestants_wrapper(ranking: Ranking):
    def wrapped(**kwargs):
        for contestant in ranking.ranking:
            print(contestant.p1, contestant.p2, contestant.p3)

    return wrapped


def insert_contestant_wrapper(ranking: Ranking):
    def wrapped(p1, p2, p3, position, **kwargs):
        p1 = int(p1)
        p2 = int(p2)
        p3 = int(p3)
        position = int(position)
        try:
            ranking.insert_contestant(p1, p2, p3, position)
        except ValueError as e:
            print(OutputColors.FAIL + e + OutputColors.ENDC)

    return wrapped


def remove_at_position_wrapper(ranking: Ranking):
    def wrapped(position, **kwargs):
        position = int(position)
        try:
            ranking.remove_contestant(position)
        except IndexError:
            print(OutputColors.FAIL + "Position is greater than the current contestant number" + OutputColors.ENDC)

    return wrapped


def remove_from_to_position_wrapper(ranking: Ranking):
    def wrapped(start_position, end_position, **kwargs):
        start_position = int(start_position)
        end_position = int(end_position)
        if start_position >= len(ranking.contestants) or end_position >= len(ranking.contestants):
            print(OutputColors.FAIL + "Position is greater than the current contestant number" + OutputColors.ENDC)
            return
        if start_position > end_position:
            print(OutputColors.WARNING + "No contestant will be removed" + OutputColors.ENDC)
            return
        try:
            ranking.remove_contestant_start_to_end(start_position, end_position+1)
        except IndexError:
            print(OutputColors.FAIL + "Position is greater than the current contestant number" + OutputColors.ENDC)

    return wrapped


def remove_filter_contestants_wrapper(ranking: Ranking):
    def wrapped(sign, score, **kwargs):
        score = int(score)
        indexes: List[int] = []
        if sign == '<':
            for index in range(len(ranking.contestants)):
                if ranking.contestants[index].average < score:
                    indexes.append(index)
        elif sign == '=':
            for index in range(len(ranking.contestants)):
                if ranking.contestants[index].average == score:
                    indexes.append(index)
        elif sign == '>':
            for index in range(len(ranking.contestants)):
                if ranking.contestants[index].average > score:
                    indexes.append(index)
        ranking.remove_contestant_positions(indexes)

    return wrapped


def replace_problem_score_wrapper(ranking: Ranking):
    def wrapped(position, problem, score, **kwargs):
        position = int(position)
        problem = Problem(problem)
        score = int(score)
        try:
            ranking.replace_problem_score(position, problem, score)
        except IndexError:
            print(OutputColors.FAIL + "Position is greater than the current contestant number" + OutputColors.ENDC)
        except ValueError as e:
            print(OutputColors.FAIL + e + OutputColors.ENDC)

    return wrapped


def average_from_to_position_wrapper(ranking: Ranking):
    def wrapped(start_position, end_position, **kwargs):
        start_position = int(start_position)
        end_position = int(end_position)
        if start_position >= len(ranking.contestants) or end_position >= len(ranking.contestants):
            print(OutputColors.FAIL + "Position is greater than the current contestant number" + OutputColors.ENDC)
            return
        if start_position > end_position:
            print(OutputColors.WARNING + "Start position is greater than end position" + OutputColors.ENDC)
            return
        sum_averages: float = 0
        for index in range(start_position, end_position+1):
            sum_averages += ranking.contestants[index].average
        sum_averages = sum_averages / (end_position - start_position)
        print(sum_averages)

    return wrapped


def minimum_from_to_position_wrapper(ranking: Ranking):
    def wrapped(start_position, end_position, **kwargs):
        start_position = int(start_position)
        end_position = int(end_position)
        if start_position >= len(ranking.contestants) or end_position >= len(ranking.contestants):
            print(OutputColors.FAIL + "Position is greater than the current contestant number" + OutputColors.ENDC)
            return
        if start_position > end_position:
            print(OutputColors.WARNING + "Start position is greater than end position" + OutputColors.ENDC)
            return
        minimum = ranking.contestants[start_position].average
        for index in range(start_position, end_position+1):
            minimum = min(minimum, ranking.contestants[index].average)
        print(minimum)

    return wrapped


def top_wrapper(ranking: Ranking):
    def wrapped(number, **kwargs):
        top = ranking.ranking
        number = int(number)
        if number > len(top):
            print("Top Number greater than the length of contestants")
            return
        for index in range(number):
            print('{}.'.format(index), top[index].p1, top[index].p2, top[index].p3, top[index].average)

    return wrapped


def top_problem_wrapper(ranking: Ranking):
    def wrapped(number, problem, **kwargs):
        number = int(number)
        problem = Problem(problem)
        top = []
        if number > len(ranking.contestants):
            print("Top Number greater than the length of contestants")
        if problem == Problem.P1:
            top = sorted(ranking.contestants, key=lambda item: item.p1, reverse=True)
        elif problem == Problem.P2:
            top = sorted(ranking.contestants, key=lambda item: item.p2, reverse=True)
        elif problem == Problem.P3:
            top = sorted(ranking.contestants, key=lambda item: item.p3, reverse=True)
        for index in range(number):
            print('{}.'.format(index), top[index].p1, top[index].p2, top[index].p3, top[index].average)

    return wrapped


def undo_wrapper(undoable_ranking: UndoableRanking):
    def wrapped():
        if undoable_ranking.undo():
            print("Last operation has been undone!")
        else:
            print("We're back to the original value!")

    return wrapped
