import { User } from "mytrack-data-classes";
import * as moment from 'moment-timezone';

moment.tz.setDefault("America/New_York");

export class NotificationHandler {
    // Check user preference
    // context-based
    // special case: weekly and sunday survey
    public static async sendContextBasedNotification(user: User, date = moment()){
        // console.log(user.prefs["sunday"]);
        // user.lunch_prefs
        // user.dinner_prefs
        // user.weight_prefs
        // user.prefs
    }

    public static getNotificationType(date = moment()): String{
        let notificationType: String = "";
        // get time of the day
        const actualtime = moment();
        const day = moment().startOf("day");
        const hour = moment().startOf("hour");
        const minute = moment().startOf("minute");
        console.log(actualtime);
        console.log(day);
        // console.log(typeof hour);
        // console.log(typeof hour.toDate());
        console.log(hour.toString());
        console.log(minute);

        return notificationType;
    }
}