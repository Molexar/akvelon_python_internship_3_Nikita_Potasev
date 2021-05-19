from django.contrib.auth.models import User
from django.db import models
from django.db.models import RESTRICT


# I will use default django's User model. That will allow easy to extend(using more fields) our model if we need
# and its contains many useful features, such as auth(its saves time for writing it by ourself)


class Transaction(models.Model):  # Implementing object Transaction with user, amount, date(only date) fields
    user = models.ForeignKey(User, on_delete=RESTRICT)
    amount = models.IntegerField()
    date = models.DateField()

    # Overriding standard method for displaying object
    def __str__(self):
        return str(self.user.id) + ':' + str(self.amount)
