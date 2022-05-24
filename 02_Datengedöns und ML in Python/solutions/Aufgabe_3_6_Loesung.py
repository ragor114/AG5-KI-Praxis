y_fit = clf.predict(X_test)
from sklearn.metrics import confusion_matrix
f, ax = plt.subplots(1,1,figsize=(16,16))
mat = confusion_matrix(y_test, y_fit)
sns.heatmap(mat.T,
            square=False,
            annot=True,
            fmt='d',
            cbar=False,
            xticklabels=["versicolor", "virginica", "setosa"], 
            yticklabels=["versicolor", "virginica", "setosa"],
            ); 
plt.xlabel('tatsächliches Label')
plt.ylabel('vorhergesagets Label'); 