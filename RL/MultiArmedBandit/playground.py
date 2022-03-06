from datetime import datetime
# from firebase_admin import firestore
# from .models import User
import pytz
from bandit.bandit import Bandit

if __name__ == "__main__":
    # date = datetime(2020, 1, 8).replace(tzinfo=pytz.UTC)
    # print(date)
    # daysSinceEpoch = (datetime.now().replace(tzinfo=pytz.UTC) - datetime(1970,1,1).replace(tzinfo=pytz.UTC)).days
    # daysSinceEpochUTC = (datetime.utcnow() - datetime(1970,1,1)).days
    # daysSinceEpochTest = (datetime(2019,12,11) - datetime(1970,1,1)).days
    # daysSinceEpochTestUTC = (datetime(2020,10,25).replace(tzinfo=pytz.UTC) - datetime(1970,1,1).replace(tzinfo=pytz.UTC)).days
    # print(daysSinceEpoch)
    # print(daysSinceEpochUTC)
    # print(daysSinceEpochTest)
    # print(daysSinceEpochTestUTC)

    # viewing website optimization as a multi-armed bandit problem
    bandit = Bandit(5)
