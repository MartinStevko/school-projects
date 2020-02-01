import math

class TweenFunc:

    @staticmethod
    def linear(time, start, change, duration):
        return change*time/duration + start

    @staticmethod
    def ease_in_quad(time, start, change, duration):
        time /= duration
        return change*time*time + start

    @staticmethod
    def ease_in_cubic(time, start, change, duration):
        time /= duration
        return change*time*time*time + start

    @staticmethod
    def ease_out_quad (time, start, change, duration):
        time /= duration
        return -change * time* (time-2) + start

    @staticmethod
    def ease_in_out_quad (time, start, change, duration):
        time /= duration/2
        if time < 1:
            return change/2*time*time + start
        time -= 1
        return -change/2 * (time*(time-2) - 1) + start

    @staticmethod
    def ease_in_out_sine(time, start, change, duration):
        return change * math.sin(time/duration * (math.pi/2)) + start


class TweenData:

    def __init__(self, target, value_start, value_end, time, tween_func, on_update, on_complete = None):
        self.on_update = on_update
        if self.on_update == None:
            self.on_update = self._on_update
        self.on_complete = on_complete
        if self.on_complete == None:
            self.on_complete = self._on_complete
        self.target = target
        self.value_start = value_start
        self.value_end = value_end
        self.time = time
        self.tween_func = tween_func
        self.current_time = 0

    def _inject_owner(self, tweens):
        self.owner = tweens

    @staticmethod
    def _on_update(target, progress, value):
        pass

    @staticmethod
    def _on_complete(target, progress, value):
        pass

    def tick(self, dt):
        self.current_time += dt

        if self.current_time >= self.time:            
            self.finish()
        else:            
            progress = self.current_time / self.time
            value = self.tween_func(self.current_time, self.value_start, self.value_end - self.value_start, self.time)
            self.on_update(self.target, progress, value)

    def finish(self):
        self.current_time = self.time
        progress = 1
        value = self.value_end
        self.on_update(self.target, progress, value)
        self.owner.stop(self)
        self.on_complete(self.target, progress, value)            

class Tween:

    def __init__(self):
        self.tweens = {}

    def tween(self, target, value_start, value_end, time, tween_func, on_update, on_complete = None):
        data = TweenData(target, value_start, value_end, time, tween_func, on_update, on_complete)
        if not (target in self.tweens.keys()):
            self.tweens[target] = []
        self.tweens[target].append(data)
        data._inject_owner(self)
        return data

    def tick(self, dt):
        for target in self.tweens:
            for tween_data in self.tweens[target]:
                tween_data.tick(dt)

    def finish(self, tween_data):
        tween_data.finish()        

    def stop(self, tween_data):
        self._remove(tween_data)

    def finish_all(self, target):
        if not (target in self.tweens.keys()):
            return
        for data in self.tweens[target]:
            data.finish()
        del self.tweens[target]

    def stop_all(self, target):
        if not (target in self.tweens.keys()):
            return
        del self.tweens[target]

    def _remove(self, tween_data):
        if not (tween_data.target in self.tweens.keys()):
            return
        self.tweens[tween_data.target].remove(tween_data)

