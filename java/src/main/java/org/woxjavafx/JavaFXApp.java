package org.woxjavafx;

import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Paths;
import java.util.Optional;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;
import org.woxjavafx.helpers.DataLoader;

public class JavaFXApp extends Application {

  @Override
  public void start(Stage stage) throws IOException {
    Optional<InputStream> iconStream =
        Optional.ofNullable(getClass().getResourceAsStream("/icon.png"));
    iconStream.ifPresent(inputStream -> stage.getIcons().add(new Image(inputStream)));
    Parent root = new FXMLLoader(getClass().getResource("/primary.fxml")).load();
    Scene scene = new Scene(root);
    stage.setScene(scene);
    stage.show();
  }

  public static void main(String[] args) throws IOException {
    DataLoader.loadData(Paths.get("/json"));
    launch();
  }
}
