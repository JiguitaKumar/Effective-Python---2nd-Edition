#Item 45 - @property vs Refactoring attributes
#Example
from datetime import datetime, timedelta

class Bucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0
    
    def __repr__(self):
        return f'Bucket(quota={self.quota})'

def fill(bucket, amount):
    now = datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount

#each time a quota consumer wants to do something, it must first ensure that
#it can deduct the amount of quota it needs to use
def deduct(bucket, amount):
    now = datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True

bucket = Bucket(60)
print(bucket)
fill(bucket, 100)
print(bucket)

if deduct(bucket, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')
print(bucket)

if deduct(bucket, 3):
    print('Had 3 quota')
else:
    print('Not enough for 3 quota')
print(bucket)

#giving the user more info: Not enough quota or the bucket was never filled
class NewBucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0
    
    def __repr__(self):
        return (f'NewBucket(max_quota = {self.max_quota},'
                f'quota_consumed = {self.quota_consumed})')

#to match the previous interface of the original bucket, lets use @property

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed
    
    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            #Quota reset for new period
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            #Quota being filled for new period
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            #Quota being consumed during the period
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta

bucket = NewBucket(60)
print('Initial', bucket)
fill(bucket, 100)
print('Filled', bucket)

if deduct(bucket, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')
print('Now', bucket)

if deduct(bucket, 3):
    print('Had 3 quota')
else:
    print('Not enough for 3 quota')
print('Now', bucket)