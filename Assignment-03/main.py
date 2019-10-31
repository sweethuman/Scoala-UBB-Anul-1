from cli import Engine
from contestant import Contestant
from ranking import UndoableRanking
from ui_wrappers import add_contestant_wrapper, list_contestants_wrapper, list_filter_contestants_wrapper, \
    list_sorted_contestants_wrapper, insert_contestant_wrapper, remove_at_position_wrapper, \
    remove_from_to_position_wrapper, remove_filter_contestants_wrapper, replace_problem_score_wrapper, \
    average_from_to_position_wrapper, minimum_from_to_position_wrapper, top_wrapper, top_problem_wrapper, undo_wrapper


def start():
    ranking = UndoableRanking([Contestant(2, 2, 2), Contestant(1, 1, 1), Contestant(3, 5, 6),
                               Contestant(3, 3, 3), Contestant(9, 9, 9), Contestant(4, 4, 4),
                               Contestant(7, 7, 7), Contestant(6, 1, 0), Contestant(6, 6, 6),
                               Contestant(0, 0, 0), Contestant(5, 5, 5)])
    engine = Engine()

    engine.command('add', 'Adds a contestant') \
        .variation('<p1:int> <p2:int> <p3:int>', add_contestant_wrapper(ranking))

    engine.command('list', 'Lists all contestants and their score') \
        .variation('', list_contestants_wrapper(ranking)) \
        .variation('<sign:(<|=|>)> <score:int>', list_filter_contestants_wrapper(ranking)) \
        .variation('sorted', list_sorted_contestants_wrapper(ranking))

    engine.command('insert', 'Insert contestant at position') \
        .variation('<p1:int> <p2:int> <p3:int> at <position:int>', insert_contestant_wrapper(ranking))

    engine.command('remove', 'Remove contestant from list') \
        .variation('<position:int>', remove_at_position_wrapper(ranking)) \
        .variation('<start_position:int> to <end_position:int>', remove_from_to_position_wrapper(ranking)) \
        .variation('<sign:(<|=|>)> <score:int>', remove_filter_contestants_wrapper(ranking))

    engine.command('replace', 'Replace score of a problem for a contestant') \
        .variation('<position:int> <problem:(P1|P2|P3)> with <score:int>',
                   replace_problem_score_wrapper(ranking))

    engine.command('avg', 'The average of the average scores for participants between positions') \
        .variation('<start_position:int> to <end_position:int>', average_from_to_position_wrapper(ranking))

    engine.command('min', 'The lowest average score of the participants between positions') \
        .variation('<start_position:int> to <end_position:int>', minimum_from_to_position_wrapper(ranking))

    engine.command('top', 'The Top Contestants') \
        .variation('<number:int>', top_wrapper(ranking)) \
        .variation('<number:int> <problem:(P1|P2|P3)>', top_problem_wrapper(ranking))

    engine.command('undo', 'Undoes the last operation') \
        .variation('', undo_wrapper(ranking))

    engine.show()


start()
