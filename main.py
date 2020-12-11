with open("input.txt") as file:
    data = file.read().split("\n")

LAST_ROW = len(data) - 1
LAST_COLUMN = len(data[0]) - 1


def seat_reorganizer(original_chart):
    new_chart = []
    for row in range(LAST_ROW + 1):
        new_chart.append([])
        for column in range(LAST_COLUMN + 1):
            if original_chart[row][column] == ".":
                new_chart[row].append(".")
                continue
            seats = []
            if row > 0:
                if column > 0:
                    seats.append(original_chart[row - 1][column - 1])
                seats.append(original_chart[row - 1][column])
                if column < LAST_COLUMN:
                    seats.append(original_chart[row - 1][column + 1])
            if row < LAST_ROW:
                if column > 0:
                    seats.append(original_chart[row + 1][column - 1])
                seats.append(original_chart[row + 1][column])
                if column < LAST_COLUMN:
                    seats.append(original_chart[row + 1][column + 1])
            if column > 0:
                seats.append(original_chart[row][column - 1])
            if column < LAST_COLUMN:
                seats.append(original_chart[row][column + 1])

            occupied = 0
            for seat in seats:
                if seat == "#":
                    occupied += 1
            if occupied == 0:
                new_chart[row].append("#")
            elif (occupied >= 4) & (original_chart[row][column] == "#"):
                new_chart[row].append("L")
            else:
                new_chart[row].append(original_chart[row][column])
        new_chart[row] = "".join(new_chart[row])
    return new_chart


def occupied_seat_counter(data):
    count = 0
    for line in data:
        count += len(line) - len(line.replace("#", ""))
    return count


new_chart = seat_reorganizer(data)

while new_chart != seat_reorganizer(new_chart):
    new_chart = seat_reorganizer(new_chart)

print(occupied_seat_counter(new_chart))
