# Intent

* An intent is an **abstract description** of an **operation to be performed**
* Its most significant use is in the launching of activities, where it can be thought of as the glue between activities

## Intents and Intent Filters

* a messaging object
  * use to request an action from another app component
* three fundamental use cases
  * Starting an activity
    * An **Activity** represents a **single screen** in an app
    * start a new instance of an Activity
      * by **passing an Intent to startActivity()**
      * The Intent **describes the activity to start** and **carries any necessary data**
  * Starting a service
    * A **Service** is a component that performs operations in the background without a user interface.
      * startService()
      * bindService()
  * Delivering a broadcast
    * A **broadcast** us a message that any app can receive.
    * The system delivers various broadcasts for **system events**
    * deliver a broadcast to other apps
      * by passing an Intent to sendBroadcast()

## PendingIntent

* A description of an Intent and **target action** to perform with it
  * the returned object can be handed to other applications
  * they can perform the action described
* It is simply a reference to a token maintained by the system describing the original data used to retrieve it
  * if its owning application's process is killed, the PendingIntent itself will remain usable from other processes that have been given it
  * call cancel() to remove it
