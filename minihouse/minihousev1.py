from minihouse.minihousemodel import state_class, item_object, move, open, close, pick, place
def test_case_0 ():
    instruction = "move the apple to the table"

    goal_state = state_class(
        robot_agent=None,
        human_agent=None,
        object_list={"apple": item_object("apple", True, "table")},
        container_list=None,
        surface_list=None,
        room_list=None,
    )

    ROOM_LIST = [
        "living room",
        "kitchen",
        "bedroom",
        "bathroom",
    ]

    OBJECT_LIST = [
        "apple",
        # "t-shirt",
        # "cup"
    ]

    OBJECT_POSITION_LIST = {
        "apple": "fridge",
        # "t-shirt": "closet",
        # "cup": "table",
    }

    CONTAINER_LIST = [
        "fridge",
        # "closet",
        # "shelf",
    ]

    SURFACE_LIST = [
        "table",
    ]

    CONTAINER_POSITION_LIST = {
        "fridge": "kitchen",
        # "closet": "bedroom",
        "table": "living room",
        # "shelf": "living room",
    }

    CONNECTED_ROOM = {
        "kitchen": ["living room"],
        "bedroom": ["bathroom", "living room"],
        "bathroom": ["bedroom"],
        "living room": ["kitchen", "bedroom"],
    }

    ACTION_DICT = {
        "move": move,
        "open": open,
        "close": close,
        "pick": pick,
        "place": place,
    }

    GROUNDED_ACTION_LIST = [
        "open fridge",
        "close fridge",
        "pick apple",
        "place apple fridge",
        "place apple table",
        "place apple bedroom",
        "place apple bathroom",
        "place apple living room",
        "move living room",
        "move kitchen",
        "move bedroom",
        "move bathroom",
    ]


    return instruction, goal_state, (ROOM_LIST, OBJECT_LIST, OBJECT_POSITION_LIST, \
    CONTAINER_LIST, SURFACE_LIST, CONTAINER_POSITION_LIST, CONNECTED_ROOM, \
    ACTION_DICT, GROUNDED_ACTION_LIST)

test_cases = [test_case_0()]
