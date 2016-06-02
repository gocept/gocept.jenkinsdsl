
// The final composition of the jobs in done in the following part.
out.println('COPY NEXT LINE MANUALLY TO POST-BUILD-ACTIONS')

for (config in configs) {
    out.print(config.name + ',')

    if (config.builder.type == 'matrixJob') {
        job = matrixJob(config.name)
    }
    else {
        job = freeStyleJob(config.name)
    }
    job.with {
        description(config.description)
        if (config.disabled == 'true') {
            disabled()
        }
    }

    config.vcs.create_config(job, config)
    config.builder.create_config(job, config)
    if (config.redmine) {
       config.redmine.create_config(job, config)
    }
}
out.println()