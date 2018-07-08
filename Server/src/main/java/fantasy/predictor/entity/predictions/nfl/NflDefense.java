package fantasy.predictor.entity.predictions.nfl;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "nfl_defense")
public class NflDefense {
  @Id
  private String name;

  private int sack;
  private int interceptions;
  private int fumRec;
  private int safeties;
  private int td;
  private int twoPtReturn;
  private int retTd;
  private int ptsAllow;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public int getSack() {
    return sack;
  }

  public void setSack(int sack) {
    this.sack = sack;
  }

  public int getInterceptions() {
    return interceptions;
  }

  public void setInterceptions(int interceptions) {
    this.interceptions = interceptions;
  }

  public int getFumRec() {
    return fumRec;
  }

  public void setFumRec(int fumRec) {
    this.fumRec = fumRec;
  }

  public int getSafeties() {
    return safeties;
  }

  public void setSafeties(int safeties) {
    this.safeties = safeties;
  }

  public int getTd() {
    return td;
  }

  public void setTd(int td) {
    this.td = td;
  }

  public int getTwoPtReturn() {
    return twoPtReturn;
  }

  public void setTwoPtReturn(int twoPtReturn) {
    this.twoPtReturn = twoPtReturn;
  }

  public int getRetTd() {
    return retTd;
  }

  public void setRetTd(int retTd) {
    this.retTd = retTd;
  }

  public int getPtsAllow() {
    return ptsAllow;
  }

  public void setPtsAllow(int ptsAllow) {
    this.ptsAllow = ptsAllow;
  }
}
