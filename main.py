import time


class Daily_routain:
    def __init__(self, breakfast_time, lunch_time, extra_lesson_time, dinner_time, night_time ):
        self.wake_time = breakfast_time
        self.lunch_time = lunch_time
        self.lesson_time = extra_lesson_time
        self.dinner_time = dinner_time
        self.night_time = night_time


    def breakfast(self):
        print(f"now at {self.wake_time} a.m. Good Morning Have a good day!!!")
        time.sleep(0.5)
        self.lunch()

    def lunch(self):
        print(f"now {self.lunch_time} a.m and lunch time!!!")
        time.sleep(0.5)
        self.lesson()

    def lesson(self):
        print(f"now {self.lesson_time} p.m . Good luck!!!")
        time.sleep(0.5)
        self.dinner()

    def dinner(self):
        print(f"now {self.dinner_time} p.m . Good evening!!!")
        time.sleep(0.5)
        self.night()

    def night(self):
        print(f"now {self.night_time} p.m. Bed time and Good Night!!!")


obj = Daily_routain("4:00", "13:30", "16:00", "19.00", "23:00")
obj.breakfast()