package fantasy.predictor.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

import fantasy.predictor.entity.keys.KickerPredictionCompositeKey;
import fantasy.predictor.entity.predictions.KickerPrediction;

public interface KickerPredictionRepository
        extends JpaRepository<KickerPrediction, KickerPredictionCompositeKey> {
  List<KickerPrediction> findBySite(String site);
}
