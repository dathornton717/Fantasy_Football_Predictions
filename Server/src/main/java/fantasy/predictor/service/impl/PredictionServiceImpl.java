package fantasy.predictor.service.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

import fantasy.predictor.entity.enums.Position;
import fantasy.predictor.entity.enums.Site;
import fantasy.predictor.entity.predictions.DefensePrediction;
import fantasy.predictor.entity.predictions.KickerPrediction;
import fantasy.predictor.entity.predictions.OffensePrediction;
import fantasy.predictor.repository.DefensePredictionRepository;
import fantasy.predictor.repository.KickerPredictionRepository;
import fantasy.predictor.repository.OffensePredictionRepository;
import fantasy.predictor.service.PredictionService;

@Service
public class PredictionServiceImpl implements PredictionService {
  private final OffensePredictionRepository offensePredictionRepository;
  private final KickerPredictionRepository kickerPredictionRepository;
  private final DefensePredictionRepository defensePredictionRepository;

  @Autowired
  PredictionServiceImpl(OffensePredictionRepository offensePredictionRepository,
                        KickerPredictionRepository kickerPredictionRepository,
                        DefensePredictionRepository defensePredictionRepository) {
    this.offensePredictionRepository = offensePredictionRepository;
    this.kickerPredictionRepository = kickerPredictionRepository;
    this.defensePredictionRepository = defensePredictionRepository;
  }

  @Override
  public List<OffensePrediction> getOffensePrediction() {
    return offensePredictionRepository.findAll();
  }

  @Override
  public List<OffensePrediction> getOffensePredictionByPosition(Position position) {
    return offensePredictionRepository.findByPosition(position.getValue());
  }

  @Override
  public List<OffensePrediction> getOffensePredictionBySite(Site site) {
    return offensePredictionRepository.findBySite(site.getValue());
  }

  @Override
  public List<OffensePrediction> getOffensePredictionByPositionAndSite(Position position, Site site) {
    return offensePredictionRepository.findByPositionAndSite(position.getValue(), site.getValue());
  }

  @Override
  public List<KickerPrediction> getKickerPrediction() {
    return kickerPredictionRepository.findAll();
  }

  @Override
  public List<KickerPrediction> getKickerPredictionBySite(Site site) {
    return kickerPredictionRepository.findBySite(site.getValue());
  }

  @Override
  public List<DefensePrediction> getDefensePrediction() {
    return defensePredictionRepository.findAll();
  }

  @Override
  public List<DefensePrediction> getDefensePredictionBySite(Site site) {
    return defensePredictionRepository.findBySite(site.getValue());
  }
}
