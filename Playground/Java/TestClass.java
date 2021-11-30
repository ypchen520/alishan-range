import java.util.function.Function;

public class TestClass {
    Function<String, Boolean> onActivity;

    public TestClass(Function<String, Boolean> onAct){
        System.out.println("this is the constructor");
        onActivity = onAct;
    }

    public void passFunc(Function<String, Boolean> onAct){
        onActivity = onAct;
    }

    public void callFunc(){
        onActivity.apply("Hello Function");
    }

    public void callCallFunc(){
        callFunc();
    }

}
