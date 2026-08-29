from spur.core.events import RelocationEvent


class Detector:
    def detect_relocations(self, previous_state, current_state):
        relocations = []

        for previous_content in previous_state:
            for current_content in current_state:
                same_content = (
                    previous_content.name == current_content.name
                    and previous_content.size == current_content.size
                )

                different_path = (
                    previous_content.path != current_content.path
                )

                if same_content and different_path:
                    event = RelocationEvent(
                        content_name=current_content.name,
                        previous_path=previous_content.path,
                        current_path=current_content.path
                    )

                    relocations.append(event)

        return relocations