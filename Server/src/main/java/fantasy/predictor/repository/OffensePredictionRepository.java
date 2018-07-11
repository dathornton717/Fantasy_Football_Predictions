package fantasy.predictor.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

import fantasy.predictor.entity.keys.OffensePredictionCompositeKey;
import fantasy.predictor.entity.predictions.OffensePrediction;

public interface OffensePredictionRepository
        extends JpaRepository<OffensePrediction,OffensePredictionCompositeKey> {
  List<OffensePrediction> findByPosition(String position);

  List<OffensePrediction> findBySite(String site);

  List<OffensePrediction> findByPositionAndSite(String position, String site);
}
