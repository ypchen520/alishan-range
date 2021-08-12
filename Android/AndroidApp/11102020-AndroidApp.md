# Android App

## Kotlin

* app > java > MainActivity
* app > res > layout > activity_main.xml
* app > manifests > AndroidManifest.xml
* Gradle Scripts > build.gradle
  * a build.gradle for the entire project
  * a build.gradle file per module

## Android developers

* [Activity](https://developer.android.com/reference/android/app/Activity)
  * There are two methods almost all subclasses of Activity will implement
  * **onCreate(Bundle)**
    * where you initialize your activity. 
    * Most importantly, here you will usually call **setContentView(int)** with a layout resource defining your UI, 
    * and using **findViewById(int)** to retrieve the widgets in that UI that you need to interact with programmatically.
  * onPause()
    * is where you deal with the user pausing active interaction with the activity. 
    * Any changes made by the user should at this point be committed
      *(usually to the **ContentProvider** holding the data).
    * In this state the activity is still visible on screen.
  * **Activity Lifecycle**
    * *activity stacks*
      * the previous activity always remains below it in the stack, and will not come to the foreground again until the new activity exits
      * There can be one or multiple activity stacks visible on screen
    * An activity has essentially four states
      * **active** or **running**
      * **visible**
        * an activity has lost focus but is still presented to the user
        * such activity is completely alive (it maintains all state and member information and remains attached to the window manager).
      * **stopped** or **hidden**
        * It still retains all state and member information, 
        * however, it is no longer visible to the user so its window is hidden
      * **destroyed**
        * The system can drop the activity from memory by either asking it to finish, or simply killing its process
        * When it is displayed again to the user, it must be completely restarted and restored to its previous state
    * state paths: **callback methods**
      * implement to perform operations when the Activity moves between states

## res

* values
