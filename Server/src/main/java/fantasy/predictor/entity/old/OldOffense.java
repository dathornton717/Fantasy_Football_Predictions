package fantasy.predictor.entity.old;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.IdClass;
import javax.persistence.Table;

import fantasy.predictor.entity.keys.OldOffenseCompositeKey;

@Entity
@Table(name = "old_offense")
@IdClass(OldOffenseCompositeKey.class)
public class OldOffense {
  @Id
  private String name;
  @Id
  private String team;
  @Id
  private String position;

  private int passYards;
  private int passTd;
  private int interceptions;
  private int rushYards;
  private int rushTd;
  private int recYards;
  private int recTd;
  private int fumTd;
  private int twoPt;
  private int fumLost;

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

  public int getPassYards() {
    return passYards;
  }

  public void setPassYards(int passYards) {
    this.passYards = passYards;
  }

  public int getPassTd() {
    return passTd;
  }

  public void setPassTd(int passTd) {
    this.passTd = passTd;
  }

  public int getInterceptions() {
    return interceptions;
  }

  public void setInterceptions(int interceptions) {
    this.interceptions = interceptions;
  }

  public int getRushYards() {
    return rushYards;
  }

  public void setRushYards(int rushYards) {
    this.rushYards = rushYards;
  }

  public int getRushTd() {
    return rushTd;
  }

  public void setRushTd(int rushTd) {
    this.rushTd = rushTd;
  }

  public int getRecYards() {
    return recYards;
  }

  public void setRecYards(int recYards) {
    this.recYards = recYards;
  }

  public int getRecTd() {
    return recTd;
  }

  public void setRecTd(int recTd) {
    this.recTd = recTd;
  }

  public int getFumTd() {
    return fumTd;
  }

  public void setFumTd(int fumTd) {
    this.fumTd = fumTd;
  }

  public int getTwoPt() {
    return twoPt;
  }

  public void setTwoPt(int twoPt) {
    this.twoPt = twoPt;
  }

  public int getFumLost() {
    return fumLost;
  }

  public void setFumLost(int fumLost) {
    this.fumLost = fumLost;
  }
}
