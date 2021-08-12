# Notification

## Add the support library

* module-level build.gradle file
  * implementation "com.android.support:support-compat:28.0.0"

## Create a basic notification

* set the notification's content and channel using a **NotificationCompat.Builder** object

## Create a channel and set the importance

```java
private void createNotificationChannel() {
  NotificationManager notificationManager = getSystemService(NotificationManager.class);
  notificationManager.createNotificationChannel(channel);
}
```

## Set the notification's tap action

* specify a content intent defined with a PendingIntent object and pass it to setContentIntent()

## Show the notification

* To make the notification appear, call NotificationManagerCompat.notify()
  * NotificationManagerCompat notificationManager = NotificationManagerCompat.from(this);
  * notificationManager.notify(notificationId, builder.build());

## Add action buttons

## Set a system-wide category

## Set lock screen visibility

## Procedure

* create a channel (createNotificationChannel) --> create a notification (NotificationCompat.Builder) --> show the notification (notificationManager.notify(notificationId, builder.build());)
