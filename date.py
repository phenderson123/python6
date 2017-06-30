import datetime
now = datetime.datetime.now()
print "-" * 25
print now
print now.year
print now.month
print now.day
print now.hour
print now.minute
print now.second

print "-" * 25

print "A week ago it was.", now - datetime.timedelta(weeks=1)

print "Like, 100 days ago it was", now - datetime.timedelta(days=100)

print "The date a week from now will be", now + datetime.timedelta(weeks=1)

print "A 1000 days from now the date will be", now +datetime.timedelta(days=1000)

print "_" * 25

birthday = datetime.datetime(2017,2,27)

print "My birthday in ...", birthday - now

print "_" * 25