package fantasy.predictor.entity.predictions.nfl;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.IdClass;
import javax.persistence.Table;

import fantasy.predictor.entity.KickerCompositeKey;
import fantasy.predictor.entity.Team;

@Entity
@Table(name = "nfl_kicker")
@IdClass(KickerCompositeKey.class)
public class NflKicker {
  @Id
  private String name;
  @Id
  private Team team;
  private int pat;
  private int teens;
  private int twenties;
  private int thirties;
  private int forties;
  private int fifties;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public Team getTeam() {
    return team;
  }

  public void setTeam(Team team) {
    this.team = team;
  }

  public int getPat() {
    return pat;
  }

  public void setPat(int pat) {
    this.pat = pat;
  }

  public int getTeens() {
    return teens;
  }

  public void setTeens(int teens) {
    this.teens = teens;
  }

  public int getTwenties() {
    return twenties;
  }

  public void setTwenties(int twenties) {
    this.twenties = twenties;
  }

  public int getThirties() {
    return thirties;
  }

  public void setThirties(int thirties) {
    this.thirties = thirties;
  }

  public int getForties() {
    return forties;
  }

  public void setForties(int forties) {
    this.forties = forties;
  }

  public int getFifties() {
    return fifties;
  }

  public void setFifties(int fifties) {
    this.fifties = fifties;
  }
}

