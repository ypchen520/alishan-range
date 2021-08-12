import java.util.ArrayList;
import java.util.Date;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.text.SimpleDateFormat;
import java.util.Arrays;

public class FileIO {
    private static List<String> log = new ArrayList<>();
    private static int peerID = 1234;
    public static void main(String[] args) throws IOException{
        String line1 = "hello";
        String line2 = "world";
        writeToLog(line1);
        writeToLog(line2);
        List<Integer> list = Arrays.asList(new Integer[]{1234, 5678, 9012, 3456});
        logPreferredNeighborsChange(list);
        writeToFile();
        logReceivingMessages(2, "interested");
        logDownloadingPiece(2, 1, 10);
        writeToFile();
        createSubDirectory();
    }
    private static void createSubDirectory(){
        try{
            File file = new File(String.valueOf(peerID));
            file.mkdir();
        }
        catch (Exception e){
            System.out.println("[FileHandler] " + e);
        }
    }
    private static void writeToFile() throws IOException{
        FileWriter fileWriter = new FileWriter("FileIO.txt", true);
        // PrintWriter printWriter = new PrintWriter(fileWriter);
        BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
        PrintWriter printWriter = new PrintWriter(bufferedWriter);
        for(String s : log){
            System.out.println(s);
            printWriter.println(s);
        }
        bufferedWriter.close();
        log = new ArrayList<>();
    }
    private static void writeToLog(String content) throws IOException{
        log.add(content);
    }

    public static void logPreferredNeighborsChange(List<Integer> preferredNeighbors) throws IOException{
        String preferredNeighborIDs = "";
        int n = preferredNeighbors.size();
        for(int i = 0; i < n; i++){
            preferredNeighborIDs += String.valueOf(preferredNeighbors.get(i));
            if(i != n-1)
                preferredNeighborIDs += ", ";
        }
        writeToLog(preferredNeighborIDs);
    }
    public static void logReceivingMessages(int peerID2, String messageType) throws IOException{
        int peerID = 0;
        final String[] setValues = new String[] { "have", "interested", "not interested" };
        final Set<String> msgTypeSet = new HashSet<>(Arrays.asList(setValues));
        if(!msgTypeSet.contains(messageType)){
            System.out.println("[logTitForTat] Unknown message type");
        }else{
            writeToLog("Peer " + peerID + " received the '" + messageType + "' message from " + peerID2 + ".");
        }
    }
    public static void logDownloadingPiece(int peerID2, int pieceIndex, int numPieces) throws IOException{
        int peerID = 0;
        writeToLog("Peer " + peerID + " has downloaded the piece " + pieceIndex + " from " + peerID2 + "." +
                   " Now the number of pieces it has is " + numPieces + ".");
    }
}