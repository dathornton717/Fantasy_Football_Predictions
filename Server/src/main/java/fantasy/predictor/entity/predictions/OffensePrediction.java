package fantasy.predictor.entity.predictions;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.IdClass;
import javax.persistence.Table;

import fantasy.predictor.entity.keys.OffensePredictionCompositeKey;

@Entity
@Table(name = "offense_prediction")
@IdClass(OffensePredictionCompositeKey.class)
public class OffensePrediction {
  @Id
  private String name;
  @Id
  private String team;
  @Id
  private String position;
  @Id
  private String site;

  private double passYards;
  private double passTd;
  private double interceptions;
  private double rushYards;
  private double rushTd;
  private double recYards;
  private double recTd;
  private double fumTd;
  private double twoPt;
  private double fumLost;

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

  public String getPosition() {
    return position;
  }

  public void setPosition(String position) {
    this.position = position;
  }

  public String getSite() {
    return site;
  }

  public void setSite(String site) {
    this.site = site;
  }

  public double getPassYards() {
    return passYards;
  }

  public void setPassYards(double passYards) {
    this.passYards = passYards;
  }

  public double getPassTd() {
    return passTd;
  }

  public void setPassTd(double passTd) {
    this.passTd = passTd;
  }

  public double getInterceptions() {
    return interceptions;
  }

  public void setInterceptions(double interceptions) {
    this.interceptions = interceptions;
  }

  public double getRushYards() {
    return rushYards;
  }

  public void setRushYards(double rushYards) {
    this.rushYards = rushYards;
  }

  public double getRushTd() {
    return rushTd;
  }

  public void setRushTd(double rushTd) {
    this.rushTd = rushTd;
  }

  public double getRecYards() {
    return recYards;
  }

  public void setRecYards(double recYards) {
    this.recYards = recYards;
  }

  public double getRecTd() {
    return recTd;
  }

  public void setRecTd(double recTd) {
    this.recTd = recTd;
  }

  public double getFumTd() {
    return fumTd;
  }

  public void setFumTd(double fumTd) {
    this.fumTd = fumTd;
  }

  public double getTwoPt() {
    return twoPt;
  }

  public void setTwoPt(double twoPt) {
    this.twoPt = twoPt;
  }

  public double getFumLost() {
    return fumLost;
  }

  public void setFumLost(double fumLost) {
    this.fumLost = fumLost;
  }
}
