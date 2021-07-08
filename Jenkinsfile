pipeline{
    options {
        skipDefaultCheckout true
    }

    agent any
    parameters{
        string(defaultValue: 'ecs_project_service', name: 'ECS_SERVICE')
        string(defaultValue: 'ecs_project', name: 'ECS_CLUSTER')
        string(defaultValue: 'eu-central-1', name: 'REGION')
        string(defaultValue: 'ecs_project-task', name: 'FAMILY', description: 'Name of task definition')
        string(defaultValue: '', name: 'REVISION', description: 'Previous version of task definition file')
        string(defaultValue: '', name: 'NEW_REVISION', description: 'New version of task definition file')
        string(defaultValue: 'web_app_td.json', name: 'PATH', description: 'Name of task definition file')
        string(defaultValue: 'master', name: 'BRANCH', description: 'Name of task definition file')
        booleanParam(name:'UPDATE_SERVICE', defaultValue: false, description: 'Update ECS service?')
    }

    stages{
        stage("Checkout to target branch"){
            steps{
                    checkout([$class: 'GitSCM', branches: [[ name: "${BRANCH}" ]], extensions : [[ $class: 'RelativeTargetDirectory', relativeTargetDir: "${BRANCH}" ]], userRemoteConfigs: [[credentialsId: 'WORK_PC', url: 'git@github.com:artem-samuilo/Task_Definition.git']]])
                }
            }
    
            
        stage("Get current Task Definition"){
            steps{
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'AWS', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh "aws ecs describe-services --service ${params.ECS_SERVICE} --cluster ${params.ECS_CLUSTER} --region ${params.REGION}"
                    sh "aws ecs describe-task-definition --task-definition ${params.FAMILY}:${params.REVISION} --region ${params.REGION}"
                }
            }
        }
        stage("Register new version of task-definition"){
            when{
                expression {
                    params.UPDATE_SERVICE
                }
            }
            steps{
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'AWS', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh "aws ecs register-task-definition --region ${params.REGION} --family ${params.FAMILY} --cli-input-json file://${params.PATH}"
                }
            }
        }
        stage("Update service"){
            when{
                expression {
                    params.UPDATE_SERVICE
                }
            }
            steps{
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'AWS', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh "aws ecs update-service --region ${params.REGION} --cluster ${params.ECS_CLUSTER} --service ${params.ECS_SERVICE} --task-definition ${params.TASK_DEFINITION}:${params.NEW_REVISION} --force-new-deployment"
                }
            }

        }
    }
}