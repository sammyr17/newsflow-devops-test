pipeline {
    agent any

    environment {
        LOG_DIR = "/tmp/newsflow-logs"
    }

    stages {
        stage('Init') {
            steps {
                script {
                    // ensure log directory exists and set timestamp for versioning artifacts
                    sh """
                        mkdir -p ${LOG_DIR}
                    """

                    env.ARTIFACT_TS = sh(
                        script: "date +%Y%m%d%H%M%S",
                        returnStdout: true
                    ).trim()
                }

                // Environment check: ensure Python 3 is available
                sh """
                    if ! command -v python3 >/dev/null 2>&1; then
                        echo 'ERROR: python3 not found in PATH'
                        exit 1
                    fi
                    python3 --version
                """
            }
        }

        stage('Test') {
            steps {
                sh """
                    echo 'Running unit tests...' | tee ${LOG_DIR}/tests-${ARTIFACT_TS}.log
                    python3 -m unittest discover -v 2>&1 | tee -a ${LOG_DIR}/tests-${ARTIFACT_TS}.log
                """
            }
        }

        stage('Verify') {
            steps {
                sh """
                    echo 'Verifying article parsing...' | tee ${LOG_DIR}/verify-${ARTIFACT_TS}.log
                    python3 article_parser.py sample_article.txt 2>&1 | tee -a ${LOG_DIR}/verify-${ARTIFACT_TS}.log
                """
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: "${LOG_DIR}/*-${ARTIFACT_TS}.log", fingerprint: true
            }
        }
    }
}
