class PointsForPlace:
    def __init__(self):
        self.points = 0

#довольно путает история с points, которая явно указана в задании, но не имеет дальнейшего использования в коде
#возможно, неверно истолковано задание

    @staticmethod
    def get_points_for_place(place):
        if 0 < place < 101:
            return 101 - place
        else:
            print('Баллы начисляются только первым 100 участникам')
            return 0


class PointsForMeters:
    def __init__(self):
        self.points = 0

#довольно путает история с points, которая явно указана в задании, но не имеет дальнейшего использования в коде
#возможно, неверно истолковано задание

    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return 0
        else:
            return meters * 0.5



class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        PointsForPlace.__init__(self)
        PointsForMeters.__init__(self)

    def get_total_points(self, meters, place):
        points_from_place = self.get_points_for_place(place)
        points_from_meters = self.get_points_for_meters(meters)
        total = points_from_place + points_from_meters
        return total



points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))