import java.util.List;
import java.util.ArrayList;

public class MyClass {
    public static void main(String args[]) {
        // Function<String, Void> handleActivity = x -> {};
        TestClass testObj = new TestClass(MyClass::handleActivity);
        // testObj.passFunc(MyClass::handleActivity);
        testObj.callFunc();
        testObj.callCallFunc();
        // TriggerClass triggerObj = new TriggerClass();
        // triggerObj.trigger();
        List<List<Object>> arrOfDiff= new ArrayList<>();
        List<Object> temp = new ArrayList<>();
        temp.add(testObj);
        temp.add(1);
        arrOfDiff.add(temp);
        double x = 1.2345;
        double y = -134.24;
        System.out.println(Math.signum(x) == Math.signum(y));
        System.out.println(Math.signum(x));
        System.out.println(Math.signum(y));
        TestClass a = (TestClass) arrOfDiff.get(arrOfDiff.size()-1).get(0);
        int b = (int) arrOfDiff.get(arrOfDiff.size()-1).get(1);
        a.callFunc();
        System.out.println(b);
        System.out.println(1000L);
    }
    public static boolean handleActivity(String activity){
        System.out.println(activity + "!!");
        return true;
    }
}