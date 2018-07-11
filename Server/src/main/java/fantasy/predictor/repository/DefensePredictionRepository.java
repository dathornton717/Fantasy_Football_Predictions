package fantasy.predictor.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

import fantasy.predictor.entity.keys.DefensePredictionCompositeKey;
import fantasy.predictor.entity.predictions.DefensePrediction;

public interface DefensePredictionRepository
        extends JpaRepository<DefensePrediction, DefensePredictionCompositeKey> {
  List<DefensePrediction> findBySite(String site);
}
