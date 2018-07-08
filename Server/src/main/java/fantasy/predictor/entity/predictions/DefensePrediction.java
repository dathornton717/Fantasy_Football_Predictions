package fantasy.predictor.entity.predictions;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.IdClass;
import javax.persistence.Table;

import fantasy.predictor.entity.keys.DefensePredictionCompositeKey;

@Entity
@Table(name = "defense_prediction")
@IdClass(DefensePredictionCompositeKey.class)
public class DefensePrediction {
  @Id
  private String name;
  @Id
  private String site;

  private double sack;
  private double interceptions;
  private double fumRec;
  private double safeties;
  private double td;
  private double twoPtReturn;
  private double retTd;
  private double ptsAllow;

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public String getSite() {
    return site;
  }

  public void setSite(String site) {
    this.site = site;
  }

  public double getSack() {
    return sack;
  }

  public void setSack(double sack) {
    this.sack = sack;
  }

  public double getInterceptions() {
    return interceptions;
  }

  public void setInterceptions(double interceptions) {
    this.interceptions = interceptions;
  }

  public double getFumRec() {
    return fumRec;
  }

  public void setFumRec(double fumRec) {
    this.fumRec = fumRec;
  }

  public double getSafeties() {
    return safeties;
  }

  public void setSafeties(double safeties) {
    this.safeties = safeties;
  }

  public double getTd() {
    return td;
  }

  public void setTd(double td) {
    this.td = td;
  }

  public double getTwoPtReturn() {
    return twoPtReturn;
  }

  public void setTwoPtReturn(double twoPtReturn) {
    this.twoPtReturn = twoPtReturn;
  }

  public double getRetTd() {
    return retTd;
  }

  public void setRetTd(double retTd) {
    this.retTd = retTd;
  }

  public double getPtsAllow() {
    return ptsAllow;
  }

  public void setPtsAllow(double ptsAllow) {
    this.ptsAllow = ptsAllow;
  }
}

