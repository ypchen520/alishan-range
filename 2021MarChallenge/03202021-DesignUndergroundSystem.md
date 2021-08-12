# Design Underground System

## Description

* Implement the UndergroundSystem class:
  * ```void checkIn(int id, string stationName, int t)```
    * A customer with a card id equal to id, gets in the station stationName at time t.
    * A customer can only be checked into one place at a time.
  * ```void checkOut(int id, string stationName, int t)```
    * A customer with a card id equal to id, gets out from the station stationName at time t.
  * ```double getAverageTime(string startStation, string endStation)```
    * Returns the average time to travel between the startStation and the endStation.
    * The average time is computed from all the previous traveling from startStation to endStation that happened directly.
    * Call to getAverageTime is always valid.
* You can assume all calls to checkIn and checkOut methods are consistent. If a customer gets in at time t1 at some station, they get out at time t<sub>2</sub> with t<sub>2</sub> > t<sub>1</sub>. All events happen in chronological order.

## Solution

### Hint

* Use two hash tables. The first to save the check-in time for a customer and the second to update the total time between two stations.
