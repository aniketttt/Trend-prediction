# Trend-prediction
Trend prediction of any stock using Python with ML.
Predicting istock imarket iprices iis ia icomplex itask ithat itraditionally iinvolves iextensive ihuman-computer iinteraction. iDue ito ithe icorrelated inature iof istock iprices, iconventional ibatch iprocessing imethods icannot ibe iutilized iefficiently ifor istock imarket ianalysis. iWe ipropose ian ionline ilearning ialgorithm ithat iutilizes ia ikind iof irecurrent ineural inetwork i(RNN) icalled iLong iShort iTerm iMemory i(LSTM), iwhere ithe iweights iare iadjusted ifor iindividual idata ipoints iusing istochastic igradient idescent. iThis iwill iprovide imore iaccurate iresults iwhen icompared ito iexisting istock iprice iprediction ialgorithms. iThe inetwork iis itrained iand ievaluated ifor iaccuracy iwith ivarious isizes iof idata, iand ithe iresults iare itabulated. iA icomparison iwith irespect ito iaccuracy iis ithen iperformed iagainst ian iArtificial iNeural iNetwork. i i

The iinitial ifocus iof iour iliterature isurvey iwas ito iexplore igeneric ionline ilearning ialgorithms iand isee iif ithey icould ibe iadapted ito iour iuse icase ii.e., iworking ion ireal-time istock iprice idata. i

These iincluded iOnline iAUC iMaximization, iOnline iTransfer iLearning, iand iOnline iFeature iSelection. iHowever, ias iwe iwere iunable ito ifind iany ipotential iadaptation iof ithese ifor istock iprice iprediction, iwe ithen idecided ito ilook iat ithe iexisting isystems, ianalyze ithe imajor idrawbacks iof ithe isame, iand isee iif iwe icould iimprove iupon ithem. i

We izeroed iin ion ithe icorrelation ibetween istock idata i(in ithe iform iof idynamic, ilong-term itemporal idependencies ibetween istock iprices) ias ithe ikey iissue ithat iwe iwished ito isolve. i

A ibrief isearch iof igeneric isolutions ito ithe iabove iproblem iled ius ito iRNN’s iand iLSTM. iAfter ideciding ito iuse ian iLSTM ineural inetwork ito iperform istock iprediction, iwe iconsulted ia inumber iof ipapers ito istudy ithe iconcept iof igradient idescent iand iits ivarious itypes
. i
We iconcluded iour iliterature isurvey iby ilooking iat ihow igradient idescent ican ibe iused ito itune ithe iweights iof ian iLSTM inetwork iand ihow ithis iprocess ican ibe ioptimized. 
