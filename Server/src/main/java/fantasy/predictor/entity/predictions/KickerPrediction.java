package fantasy.predictor.entity.predictions;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.IdClass;
import javax.persistence.Table;

import fantasy.predictor.entity.keys.KickerPredictionCompositeKey;

@Entity
@Table(name = "kicker_prediction")
@IdClass(KickerPredictionCompositeKey.class)
public class KickerPrediction {
  @Id
  private String name;
  @Id
  private String team;
  @Id
  private String site;
  private double pat;
  private double teens;
  private double twenties;
  private double thirties;
  private double forties;
  private double fifties;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public String getTeam() {
    return team;
  }

  public void setTeam(String team) {
    this.team = team;
  }

  public String getSite() {
    return site;
  }

  public void setSite(String site) {
    this.site = site;
  }

  public double getPat() {
    return pat;
  }

  public void setPat(double pat) {
    this.pat = pat;
  }

  public double getTeens() {
    return teens;
  }

  public void setTeens(double teens) {
    this.teens = teens;
  }

  public double getTwenties() {
    return twenties;
  }

  public void setTwenties(double twenties) {
    this.twenties = twenties;
  }

  public double getThirties() {
    return thirties;
  }

  public void setThirties(double thirties) {
    this.thirties = thirties;
  }

  public double getForties() {
    return forties;
  }

  public void setForties(double forties) {
    this.forties = forties;
  }

  public double getFifties() {
    return fifties;
  }

  public void setFifties(double fifties) {
    this.fifties = fifties;
  }
}
