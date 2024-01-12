from amplpy import AMPL, ampl_notebook

ampl = ampl_notebook(
    modules=["cbc", "highs"],  # modules to install
    license_uuid="default",  # license to use
)  # instantiate AMPL object and register magics

# define decision variables
ampl.eval("""
            var o >= 0;
            var c >= 0;
            var p >= 0;
            var s >= 0;
            var e >= 0;
          """)

# define objective function
ampl.eval("""
            minimize Cost:
                1.16*o + 1.78*c + 0.82*p + 4.13*s + 5.49*e;
        """)

# define constraints
ampl.eval("""
            subj to sodium: 80*c + 400*p + 90*s + 890*e <= 35000;
            subj to calories: 360*o + 270*c + 260*p + 310*s + 450*e >= 14000;
            subj to protein: 12*o + 27*c + 8*p + 31*s + 20*e >= 350;
            subj to vitd: 15.9*s + 0.8*e >= 140;
            subj to calcium: 105*o + 50*p + 390*e >= 9100;
            subj to iron: 3.2*o + 0.9*c + 1.3*p + 2.2*s + 2.3*e >= 126;
            subj to potassium: 392*o + 410*c + 580*p + 700*s + 430*e >= 32900;
        """)

# exhibit the model that has been built
ampl.eval("show;")
ampl.eval("expand;")

# solve using two different solvers
ampl.option["solver"] = "cbc"
ampl.solve()

ampl.option["solver"] = "highs"
ampl.solve()

# display a component of the model
ampl.display("Cost")
ampl.display("_varname", "_var")